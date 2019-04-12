# SQL - PostgreSQL 9.6

results = run_sql

describe :query do
    describe "should contain keywords" do
        it "should contain SELECT" do
            expect($sql.upcase).to include("SELECT")
        end

        it "should contain FROM" do
            expect($sql.upcase).to include("FROM")
        end
    end

    describe :columns do
        it "should return 2 columns" do
            expect(results.first.keys.count).to eq 2
        end

        it "should return an arms column" do
            expect(results.first.keys).to include(:arms)
        end

        it "should return a legs column" do
            expect(results.first.keys).to include(:legs)
        end
    end
end
