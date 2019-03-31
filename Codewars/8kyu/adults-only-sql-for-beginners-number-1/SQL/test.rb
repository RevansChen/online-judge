results = run_sql

describe :users do
    it "should return 4 users" do
        expect(results.count).to eq 4
    end
end
